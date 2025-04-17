# ⚖️ Lawgic AI - Legal Chatbot

[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/Powered%20By-LangChain-blue?style=for-the-badge)](https://www.langchain.com/)
[![HuggingFace](https://img.shields.io/badge/LLM-HuggingFace-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co)
[![Django](https://img.shields.io/badge/Backend-Django-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)

In India, millions of people lack access to reliable legal knowledge, often leading to uninformed decisions and unnecessary legal
trouble. Legal information is scattered, complex, and sometimes misrepresented online. Our AI-powered legal assistantis designed
to bridge this knowledge gap by providing users with accurate, verified legal insights strictly sourced from trusted books and official
legal PDFs.
By leveraging AI, we simplify complex legal terms, making them easy to understand for individuals, businesses, and organizations.
Our goal is to empower citizens with legal literacy, ensuring they can confidently navigate their rights and responsibilities without
relying on misleading sources.

---

## 🧠 Features

🤖 Chatbot Interface: Ask legal questions in plain English or Hindi.

📚 Answers legal questions based on your custom data

🧠 LLM-powered: Integrated with Hugging Face LLMs (like Mistral 7B).

📁 FAISS Vector Store: Fast and scalable document similarity search.

🧾 Cites Sources: View where the legal information was retrieved from.

🔐 Privacy-First: All queries run locally or through secure APIs.


## ⚙️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yuvraj-kumar-dev/Lawgic_AI.git
   cd Lawgic_AI
   ``

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ``

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ``

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your configuration:

   ```env
   HUGGINGFACE_API_TOKEN=your_huggingface_api_token
   ``

5. **Run the Application**

   ```bash
   python manage.py runserver
   ``

   Access the chatbot at `http://localhost:8000/chatbot/`.

---

## 🧠 Customizing the FAISS

To tailor the chatbot to your specific legal documens:

1. **Prepare Your Documents*: Gather your legal documents in `.pdf` format.**

2. **Generate Embeddings and Create FAISS Index**:

   ```python
   from langchain.vectorstores import FAISS
   from langchain.embeddings import HuggingFaceEmbeddings

   embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
   documents = [...]  # Load your documents here
   faiss_index = FAISS.from_documents(documents, embeddings)
   faiss_index.save_local("faiss_index")
   ``

3. **Update the Application*: Ensure that the application points to your new `faiss_index`.**

---

## 📄 Licene

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for detals.

---

