from Website import create_app

app = create_app()
if __name__ == '__main__': #running this will initialize create_app() turning on the server.
    app.run(debug=True)