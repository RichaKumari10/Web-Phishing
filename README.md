# 🔒 Phishing URL Detector

A machine learning-powered web application that helps detect phishing URLs in real-time. Built with Streamlit and Python, this tool analyzes URLs and determines whether they are legitimate or potentially malicious.

## 🌟 Features

- Real-time URL analysis
- Machine learning-based detection
- Detailed feature analysis
- User-friendly interface
- Confidence score for predictions
- Technical details expansion for advanced users

## 🛠️ Technology Stack

- Python 3.x
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle (for model serialization)

## 📋 Prerequisites

Before running the application, make sure you have Python installed on your system. Then install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/RichaKumari10/Web-Phishing.git
cd phishing-detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📊 How It Works

The application uses a trained machine learning model to analyze various features of the input URL, including:
- URL length and structure
- Domain information
- Security indicators
- HTML and JavaScript elements
- Network-based features

Based on these features, the model predicts whether the URL is legitimate or potentially phishing.

## 🔍 Features Analyzed

- URL and Domain Features
- HTML and JavaScript Features
- Domain-based Features
- Security Indicators
- And many more...

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. While it can help identify potential phishing URLs, it should not be the sole factor in determining the safety of a website. Always exercise caution when visiting unknown websites.

## 👥 Authors

- Richa Kumari - Initial work

## 🙏 Acknowledgments

- Thanks to all contributors and supporters
- Streamlit for the amazing framework
- The machine learning community for resources and inspiration