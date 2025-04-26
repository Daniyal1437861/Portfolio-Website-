from flask import Flask
app = Flask(__name__)

@app.route('/')
def portfolio():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Portfolio</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                padding: 20px;
            }
            h1 { color: #007BFF; }
            .section { margin-bottom: 30px; }
        </style>
    </head>
    <body>
        <h1>Welcome to My Portfolio</h1>
        <div class="section">
            <h2>About Me</h2>
            <p>Hello, I'm Ali Khan. I am a Python Developer with a passion for building web apps.</p>
        </div>

        <div class="section">
            <h2>Projects</h2>
            <ul>
                <li>Library Management System</li>
                <li>Weather Forecast App</li>
                <li>To-do List App</li>
            </ul>
        </div>

        <div class="section">
            <h2>Contact</h2>
            <p>Email: alikhan@example.com</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)