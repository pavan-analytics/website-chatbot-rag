# Website Chatbot using RAG (No API)

## 📌 Overview
This project is a console-based chatbot that interacts with a website by extracting and processing its content.  
It uses a Retrieval-Augmented Generation (RAG) approach to answer user queries based on the website data.

---

## 🚀 Features
- Web scraping using BeautifulSoup  
- Text preprocessing and chunking  
- Semantic search using embeddings  
- Vector database using FAISS  
- Context-based response generation  
- Console-based chatbot interface  

---

## 🛠 Tech Stack
- Python  
- BeautifulSoup  
- Sentence Transformers  
- FAISS  

---

## ⚙️ How It Works
1. The chatbot scrapes website content from a given URL  
2. The content is cleaned and split into smaller chunks  
3. Each chunk is converted into embeddings  
4. FAISS is used to store and search relevant chunks  
5. Based on user query, the most relevant content is retrieved and displayed  

---

## ▶️ How to Run
### 1. Clone the repository
- git clone https://github.com/pavan-analytics/website-chatbot-rag.git
- cd website-chatbot-rag

### 2. Install dependencies
pip install requests beautifulsoup4 faiss-cpu sentence-transformers

### 3. Run the chatbot
python chatbot.py

### 4. Provide website URL
Enter any valid website URL when prompted.

### 5. Ask questions
Example queries:
- What is this product used for?
- What features does this platform offer?
- Does this platform support integrations?
- What is pricing?

---

## ⚠️ Notes
- The chatbot works on **static website content**
- Some information (e.g., pricing) may not be available if loaded dynamically

---

## ⚠️ Limitations
- The chatbot works only on static website content  
- Dynamic content (like pricing loaded via JavaScript) may not be captured  

---

## 🎥 Demo
https://drive.google.com/file/d/1_Wa4QXBzpeU20IG4EmV6Gc5u81uB3Hpt/view?usp=drive_link

---

## 📌 Author
Pavan Kalyan Musham
