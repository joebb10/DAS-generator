# DAS-generator
This flask api allows you to generate and send DAS documents to WhatsApp numbers.

This code is a Flask application that generates and sends a DAS document to a WhatsApp number.

To use the application, you will need to first create a Receita Federal API key. Once you have your API key, you can start the application by running the following command:

python app.py

The application will then be available at the following URL:

http://localhost:5000/

You can generate a DAS document by sending a POST request to the following URL:

http://localhost:5000/generate-das

The request body should contain the following JSON data:

{
  "nome": "John Doe",
  "cnpj": "12345678901234",
  "whatsapp": "1234567890"
}

The application will then generate the DAS document and send it to the specified WhatsApp number.


