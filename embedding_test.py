from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

sentences = [
    "آج موسم اچھا ہے",
    "آج بارش ہو رہی ہے",
    "موسم بہت گرم ہے",
    "مجھے مدد کی ضرورت ہے",
    "میں AI سیکھ رہا ہوں",
    "پاکستان خوبصورت ملک ہے",
    "کتاب میز پر ہے",
    "مجھے چائے پسند ہے",
    "وہ اسکول جا رہا ہے",
    "آج بہت خوشی کا دن ہے"
]

embeddings = model.encode(sentences)

sim = util.cos_sim(embeddings[0], embeddings[1])
print("Similarity between sentence 1 and 2:", sim.item())