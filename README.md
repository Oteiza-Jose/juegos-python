<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PyFunZone 🐍</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #3b5998 3px solid;
        }
        header a {
            color: #fff;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 16px;
        }
        header ul {
            padding: 0;
            list-style: none;
        }
        header li {
            float: left;
            display: inline;
            padding: 0 20px 0 20px;
        }
        header #branding {
            float: left;
        }
        header #branding h1 {
            margin: 0;
        }
        header nav {
            float: right;
            margin-top: 10px;
        }
        #showcase {
            min-height: 400px;
            background: #35424a;
            color: #fff;
            text-align: center;
            padding: 100px 20px;
        }
        #showcase h1 {
            margin-top: 40px;
            font-size: 55px;
            margin-bottom: 10px;
        }
        #showcase p {
            font-size: 20px;
        }
        #boxes {
            margin-top: 20px;
        }
        #boxes .box {
            float: left;
            width: 30%;
            padding: 10px;
            text-align: center;
        }
        #boxes .box img {
            width: 90px;
        }
        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 30px 0 0;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div id="branding">
                <h1>PyFunZone 🐍</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="#">Inicio</a></li>
                    <li><a href="#">Juegos</a></li>
                    <li><a href="#">Acerca de</a></li>
                    <li><a href="#">Contacto</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="showcase">
        <div class="container">
            <h1>Bienvenido a PyFunZone 🐍</h1>
            <p>Explora nuestros emocionantes juegos creados con Python y Tkinter</p>
        </div>
    </section>

    <section id="boxes">
        <div class="container">
            <div class="box">
                <img src="https://via.placeholder.com/90" alt="Minesweeper">
                <h3>Buscaminas</h3>
                <p>Desafía tus habilidades estratégicas y trata de no explotar una mina.</p>
            </div>
            <div class="box">
                <img src="https://via.placeholder.com/90" alt="Tic Tac Toe">
                <h3>Cruz y Círculo</h3>
                <p>Compite contra la máquina en este clásico juego de tres en línea.</p>
            </div>
        </div>
    </section>

    <footer>
        <p>PyFunZone 🐍 | Creado por José Oteiza</p>
    </footer>
</body>
</html>
