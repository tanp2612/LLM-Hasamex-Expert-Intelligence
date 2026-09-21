import os
from langchain_core.documents import Document

def load_and_chunk_transcripts(data_dir="data"):
    """
    Parses all transcript text files in the data directory, 
    dynamically extracting expert names and paragraph blocks.
    """
    docs = []
    if not os.path.exists(data_dir):
        print(f"Directory {data_dir} not found.")
        return docs

    for filename in os.listdir(data_dir):
        if filename.endswith(".txt") and "Interview_Guide" not in filename:
            # Extract expert name cleanly from "Transcript_1_France.txt" -> "France" or similar
            expert_name = filename.replace(".txt", "").replace("Transcript_", "")
            file_path = os.path.join(data_dir, filename)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Split by double newlines or single newlines to capture all text blocks
            paragraphs = content.split("\n")
            for para in paragraphs:
                if para.strip():
                    docs.append(Document(
                        page_content=para.strip(),
                        metadata={"expert": expert_name, "timestamp": "00:00"}
                    ))
                    
    print(f"Successfully loaded and chunked {len(docs)} documents from transcripts.")
    return docs

if __name__ == "__main__":
    docs = load_and_chunk_transcripts()
    print(f"Total chunks created: {len(docs)}")