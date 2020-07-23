<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="{{ mix('css/app.css') }}">
    <title>Document</title>
</head>

<body>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <a class="navbar-brand" href="/">Subject</a>
        </nav>

        <div class="container">
            <router-view></router-view>
        </div>
    </div>

    <script src="{{ mix('js/app.js') }}"></script>
</body>

</html>
