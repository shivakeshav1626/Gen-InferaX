# Gen-InferaX

**Gen-InferaX** is a **Smart Research Assistant** designed to retrieve information, reason step-by-step, and deliver accurate, structured responses using a **Large Language Model (LLM)**.  
It integrates multiple **GenAI concepts** such as prompting strategies, similarity measures, embeddings, vector databases, structured outputs, function calling, and more.

---

## **Key Features**

### **Prompt Engineering**
- Zero-shot, One-shot, Multi-shot prompting  
- Chain-of-thought prompting for step-by-step reasoning  
- Dynamic prompting to adjust based on user context  
- System and User prompt separation using the **RTFC framework**

### **LLM Behavior Control**
- Temperature, Top-K, Top-P tuning  
- Stop sequences to prevent unwanted responses  
- Structured output (JSON format)  
- Function calling to trigger external APIs or calculations  

### **Embeddings and Similarity**
- Generate embeddings for queries and documents  
- Compare embeddings using **Cosine Similarity, Dot Product, and Euclidean Distance**  
- Store and retrieve context using a **Vector Database** (FAISS, Pinecone, or Weaviate)

### **Evaluation and Monitoring**
- Token usage logging after every AI call  
- Evaluation dataset with at least 5 test cases  
- Automated testing framework with judge prompts to verify accuracy  

---

## **Tech Stack**
- **Frontend:** React (MERN Level 1 concepts)  
- **Backend:** Node.js + Express *(or Python + FastAPI if preferred)*  
- **LLM Provider:** OpenAI API / Llama 3  
- **Database:** Vector Database (FAISS or Pinecone)  
- **Version Control:** GitHub with Pull Requests for each feature implementation  

---

## **Project Overview**
Gen-InferaX serves as an end-to-end demonstration of how to build a robust GenAI system.  
It showcases:
- Advanced **prompting techniques**
- **Semantic search** using embeddings
- **Reasoning-driven responses** from LLMs
- **Evaluation pipelines** for accuracy and performance

---

