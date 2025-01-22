
# Simple Streamlit, Polars & DuckDB Project

Welcome to this simple project that integrates **Streamlit**, **Polars**, and **DuckDB** to create an interactive web application for visualizing geographic and demographic data.

## Description

This project loads data from DuckDB, processes it with Polars for optimal performance, and visualizes it using Streamlit. The app provides an intuitive interface where you can select countries and display cities with their populations on an interactive map.

[image](./img/app.png)

## Prerequisites

Make sure you have Python 3.9 or higher installed on your machine. 

## Installation

Follow the steps below to set up your environment and run the app.

### 1. Create a Virtual Environment

First, create a virtual environment to isolate the project dependencies:

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

#### On Windows

```bash
.venv\Scripts\activate
```

#### On macOS/Linux

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

Once your environment is set up and dependencies are installed, you can run the Streamlit app with the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the app at:

```html
http://localhost:8501
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
