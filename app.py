from flask import Flask, render_template, request
from prompts import PROMPTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_prompt = ""
    query = ""

    if request.method == "POST":
        if "prompt_type" in request.form:
            selected = request.form.get("prompt_type")
            selected_prompt = PROMPTS.get(selected, "Prompt not found.")
        elif "feedback" in request.form:
            idea = request.form.get("idea")
            feedback = request.form.get("feedback")
            save_feedback(idea, feedback)
            return render_template("thankyou.html")
        elif "search" in request.form:
            query = request.form.get("search").lower()
            filtered_prompts = {k: v for k, v in PROMPTS.items() if query in k.lower()}
            return render_template("index.html", prompts=filtered_prompts, result="", query=query)

    return render_template("index.html", prompts=PROMPTS, result=selected_prompt, query=query)

def save_feedback(idea, feedback):
    with open("feedback.txt", "a") as f:
        f.write(f"Idea 💡: {idea}\nFeedback 📝: {feedback}\n---\n")

@app.route("/faqs")
def faqs():
    faqs_list = [
        ("What is Dev Prompts?", "It generates useful prompts for content, design, dev tools, and more."),
        ("Is this free?", "Yes! 100% free to use."),
        ("Can I suggest my own prompts?", "Absolutely. Use the feedback form."),
        ("How do I copy a prompt?", "Click generate and select the result to copy."),
        ("Are prompts saved?", "Not yet, but future version will support user accounts."),
        ("Can I use these prompts in ChatGPT?", "Yes, they're perfect for that."),
        ("Do I need to sign in?", "No login required."),
        ("How do I join your WhatsApp?", "Click the green button at the bottom of homepage."),
        ("Will more categories be added?", "Yes, based on your feedback."),
        ("Can I request custom features?", "Yes! Drop your idea via feedback."),
        ("Where is feedback stored?", "Locally in a text file."),
        ("Will I see my submitted feedback?", "Not now, but dashboard is coming."),
        ("Can I contribute to this project?", "Yes, contact mughal.dev for collab."),
        ("Does this work on mobile?", "Fully responsive for phones and tablets."),
        ("Why is it called Dev Prompts?", "Because it’s made for developers, by a dev 🧠."),
    ]
    return render_template("faqs.html", faqs=faqs_list)

if __name__ == "__main__":
    app.run(debug=True)