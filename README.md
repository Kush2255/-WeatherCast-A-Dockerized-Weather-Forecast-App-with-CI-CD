# 🌤️ WeatherCast – A Dockerized Weather Forecast App with CI/CD

## 📄 Description
**WeatherCast** is a Flask-based web application that provides real-time weather forecasting. It uses **web scraping** to collect data from the BBC Weather website. Users can enter any city name and get high/low temperatures and a summary forecast.

---

## 🚀 Features
- ✅ Flask Web Framework
- ✅ Weather data scraping from [BBC Weather](https://www.bbc.com/weather)
- ✅ Displays:
  - 🌡️ Daily high and low temperatures
  - 📋 Daily weather summaries
- ✅ Dockerized for easy deployment
- ✅ Ready for CI/CD pipelines

---

## 🛠️ Installation & Setup

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/Kush2255/-WeatherCast-A-Dockerized-Weather-Forecast-App-with-CI-CD.git
cd -WeatherCast-A-Dockerized-Weather-Forecast-App-with-CI-CD
🔹 2. Create Virtual Environment (Optional but recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
🔹 3. Install Python Dependencies
bash
Copy
Edit
pip install flask requests beautifulsoup4 pandas
▶️ Usage
Run the Flask App
bash
Copy
Edit
python app.py
Then open your browser and go to:
➡️ http://127.0.0.1:5000

Enter the name of any city (e.g., Hyderabad, Warangal, Khammam) and click "Get Weather".

🐳 Docker Support (Optional)
🔹 Build the Docker image
bash
Copy
Edit
docker build -t weathercast .
🔹 Run the container
bash
Copy
Edit
docker run -p 5000:5000 weathercast
Then visit http://localhost:5000 in your browser.

🧩 Dependencies
Flask

Requests

BeautifulSoup4

Pandas

⚠️ Disclaimer
This project is built for educational and demonstration purposes.
Since it relies on scraping data from BBC Weather, any changes in their site structure might require updates to the scraping logic.

📷 Screenshots (Optional)
Add UI screenshots here (paste them into the repo or link to images)

👨‍💻 Author
Kushwanth Rasala
GitHub: @Kush2255

📌 License
This project is licensed under the MIT License.

💡 Built with ❤️ using Flask, Python, Docker, and DevOps best practices.

yaml
Copy
Edit

---

### ✅ What to do next:
1. Open your `README.md` file.
2. Replace all content with the above.
3. Save it.
4. Push it to GitHub:
```bash
git add README.md
git commit -m "Clean README with features, Docker, and usage"
git push origin main