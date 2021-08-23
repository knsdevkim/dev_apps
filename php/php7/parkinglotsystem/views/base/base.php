<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base Layout</title>
    <style>
        @font-face {
            font-family: defaultFont;
            src: url(<?= URL ?>public/fonts/colombia-font/Colombia-Rp0DV.ttf);
        }

        * {
            font-family: defaultFont;
        }

        p {
            font-size: 80px;
            text-align: center;
            text-transform: uppercase;
            margin: 200px auto;
        }
    </style>
</head>
<body>
    <?php pagecontent(); ?>
</body>
</html>