# Schedule-Generator
-------
Funcionamento do programa:
* Copie o horário direto da aba principal do SIGAA.

<img width = "70%" src = "/util/print_sigaa.png">

* Sobreescreva o que foi copiado no arquivo `data/subjects.txt`.
* Execute o script `script.sh`:
    ```bash
        bash script.sh
    ```
* Um arquivo HTML foi criado: `css_html/index.html`, assim como seu CSS dinâmico `css_html/table_content_style.css`.
* O arquivo `css_html/index.html` será automaticamente convertido em imagem e armazenado no diretório `img`.
* Caso deseje ter a imagem enviada para algum grupo do Telegram, adicione o bot `@horaio_bot` no grupo, e execute o script desta maneira:
    ```bash
        bash script.sh chat_id
    ```
    onde `chat_id` é o id do chat do grupo em questão.
