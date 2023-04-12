from website import create_app

app = create_app()

if __name__ == '__main__': # Lines below will run only if we RUN this file, NOT IMPORT this file
    app.run(debug=True) # Everytime we will make a change in our python code, it will automatically rerun the webserver 
                        # From the documentation: "Do not run the development server or debugger in a production environment"
                        