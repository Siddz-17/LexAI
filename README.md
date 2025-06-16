# 🎬 LexAI

LexAI is an intelligent YouTube video summarizer that transforms lengthy videos into concise, insightful summaries within seconds. Powered by Groq and visually represented to you using Streamlit, LexAI helps you grasp key points quickly and even allows you to ask specific questions about the video content.

## 🚀 Features

- **YouTube Video Summarization:** Instantly generate concise summaries of YouTube videos.
- **Interactive Q&A:** Ask questions based on the generated summary and receive clear, specific answers.
- **Dynamic Typing Effect:** Enjoy a visually engaging typing animation while the summary is generated.
- **Video Information Display:** Automatically fetches and displays the video’s title and thumbnail.
- **Modern UI:** Clean and responsive interface with a sleek gradient background and customized buttons.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend Services/APIs Consumed:** Python (Groq API, YouTube Transcript API)
- **AI Model:** LLama3-70b and LLama3-8b (via Groq API)
- **Key Python Libraries:**
  - `streamlit` for the application interface
  - `youtube-transcript-api` for fetching video transcripts
  - `aiohttp` for asynchronous operations (used by `youtube-transcript-api`)
  - `groq` for interacting with the Groq API
  - `python-dotenv` for local environment variable management

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/siddz-17/lexai.git
   cd lexai
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables (for local execution):**
   Create a `.env` file in the project root with your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
   (The application loads this key using `python-dotenv`.)

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## 🌐 Usage

1. Ensure you have followed the installation steps and the app is running.
2. Open your web browser and navigate to the local Streamlit URL (usually `http://localhost:8501`).
3. Enter the YouTube video URL in the input field.
4. Click **"Summarize Video"** to generate the summary.
5. View the video title, thumbnail, and dynamic summary.
6. Ask specific questions about the summary for detailed answers.

## 🚀 Deploying to Streamlit Community Cloud

This application is ready to be deployed using Streamlit Community Cloud!

1.  **Prerequisites:**
    *   Ensure your code is pushed to a GitHub repository.
    *   You will need your `GROQ_API_KEY`.

2.  **Deployment Steps:**
    *   Go to [share.streamlit.io](https://share.streamlit.io/).
    *   Click "Deploy an app".
    *   Connect your GitHub account and select the repository and branch for this application.
    *   The main application file is `app.py` and the `requirements.txt` is already configured.
    *   **Important:** Before deploying, go to the "Advanced settings..." section and add your `GROQ_API_KEY` to the "Secrets" manager. The key name should be `GROQ_API_KEY` and the value should be your actual API key. This is how Streamlit Cloud securely manages your API key.
    *   Click "Deploy!".

Your app should now be live. For more detailed instructions, refer to the [official Streamlit deployment guide](https://docs.streamlit.io/sharing-your-app/deploy-your-app).

## 🤖 AI Models

The application utilizes the following models via the Groq API:
- **LLama3-70B:** Used for detailed summarization.
- **LLama3-8B:** Optimized for answering questions quickly.

## 📝 Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💬 Acknowledgements

- **Groq** for providing access to powerful AI models like LLama3.
- **Streamlit** for the easy-to-use web application framework.
- **YouTube Transcript API** for seamless transcript extraction.

---

Built with ❤️. (You can add your name/GitHub profile here if you wish)
