from website import create_app #__init__.py allows the website folder to be referenced

app = create_app()

if __name__ == '__main__': 
    app.run(debug= True)
