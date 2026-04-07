import requests
from bs4 import BeautifulSoup
import numpy as np
import faiss

# ===== EMBEDDING MODEL =====
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode(text)


# ===== STEP 1: SCRAPE WEBSITE =====
def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unnecessary tags
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        text = soup.get_text(separator=" ")
        return text

    except Exception as e:
        print("❌ Error scraping website:", e)
        return ""


# ===== STEP 2: CHUNK TEXT =====
def chunk_text(text, chunk_size=150):
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]


# ===== STEP 3: CREATE VECTOR STORE =====
def create_vector_store(chunks):
    print("🔄 Creating embeddings...")

    embeddings = [get_embedding(chunk) for chunk in chunks]
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index


# ===== STEP 4: SEARCH =====
def search(query, chunks, index, k=3):
    query_embedding = np.array([get_embedding(query)]).astype("float32")
    _, indices = index.search(query_embedding, k)

    return [chunks[i] for i in indices[0]]


# ===== STEP 5: CHATBOT RESPONSE (NO API) =====
def ask_chatbot(query, chunks, index):
    context_chunks = search(query, chunks, index)

    if not context_chunks:
        return "I don't know based on the website content."

    best_context = context_chunks[0]

    # Remove common useless words
    stopwords = {"what", "is", "the", "of", "in", "on", "a", "an", "and", "to", "for"}
    keywords = [word.lower() for word in query.split() if word.lower() not in stopwords]

    lines = best_context.split(".")

    relevant_lines = []
    for line in lines:
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in keywords):
            relevant_lines.append(line.strip())

    if relevant_lines:
        return "Based on the website:\n\n" + ". ".join(relevant_lines[:2])
    else:
        return "I couldn't find exact information, but here's the closest:\n\n" + best_context


# ===== STEP 6: MAIN CHAT LOOP =====
def run_chatbot(url):
    print("\n🔍 Scraping website...")
    text = scrape_website(url)

    if not text.strip():
        print("❌ Failed to fetch website content.")
        return

    print("✂️ Processing content...")
    chunks = chunk_text(text)

    print(f"📊 Total chunks created: {len(chunks)}")

    index = create_vector_store(chunks)

    print("\n🤖 Chatbot Ready! Type 'exit' to quit.\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("👋 Exiting chatbot.")
            break

        answer = ask_chatbot(query, chunks, index)
        print("\nBot:", answer, "\n")


# ===== ENTRY POINT =====
if __name__ == "__main__":
    url = input("Enter website URL: ")
    run_chatbot(url)