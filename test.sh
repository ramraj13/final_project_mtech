#!/bin/bash

# Replace these variables with your actual RSA private key and encrypted message
RSA_PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
MIIEoQIBAAKCAQEAq1F/zW5Lk8nRsYGsfRfox8Ff6MB2+rfl43p7ISIjYpEaD3SF
1pZ+FmDBQpEucET7V6SofBNx54OTbbt2I+J4teJzfsm7pyFagiOpbrvjPXuAI6k0
FPswsGVUoM5Mw+qRs/0NLzrBVw1xMCbi64xDePcPwXX3PnnMhen680ZM1cfbJac2
FhconJ4+JLjRoxusPCL4iwte8Ciu8uLPnOzzOgs9GSgTZU20J3gfKWVMgKhF0DMU
bRvUM9HfMiGV6DyG/catbMYaYyJmUeCH5p1hLHaHAlYbHylw1di+P7iwaX/rkrlz
RkRzQofaqEUczWDZnLnNez4+CANUUCFwjDKjWwIDAQABAoH/KZxpsOeExcw6Md4K
sEMjibMrxorP9OzAF81RBmQquTGuMh0L6iKExUbZqg7rPcAS5f5vfU0nTg8dFwoQ
CSxkWJYJbTgDLil2AG29gUGH/59McQsJTp6qJXXTb2Ru5KxNKCf3i9g5jkymLEQ7
c0KZNVKkAQyWtD7/7j8pNO2bxjw6N0huQwCHv3h/1DV5OQtmem5lj/Ori4cvh+61
jcDe76bOgVN5GLZov8Dh8CmNsLEuppY7cQ632RJ5lAqzZI8XZcZXH2X6CjC7xFsd
ubY1eBk1T+RaQzYxwkoMeRr9B4PKnvTBLafUUFGEDbPckVDJ6ITbN1iDk0AUwDTs
nfZVAoGBALW8pBOu6qcaCaHV95yg+Vkc/9LCdR1V/c1eqUOzG6N1rrcGaCHziSqe
3JFYnXc4chm1xXps+t+EJy7gWf1SfObioG0XJs5g57AMK4LVRGm4xMONYUnzF7Bm
2d7s9DVYAmaVu73baX3wD/7BhMY7QwNUL6BL/yV5XQLkYtO6G/sNAoGBAPFS/AaN
aPpDldDX0dR0reF6kj9A72GQS0eap7gF4qq3GCsuck1oxQH+Lj0ny6fHKMgg+mTF
35PUg2ZqfuRxmg9yPc9KQ7xUirGB3DOVzYDgWudljrG9d4nhMD7pjx4LOBogXebt
fU3iH01mt3cizWeEnhWSirncR7kVlUwcQF4HAoGAdUTply3qirM5fe1knvQckg0t
YqFKEwj3AftQO7gqYHrCp6WBsk7EtvTVnRBSY6jPr5lkeVAzPeG3qv7n8pe0swOP
w3UJ/Gf5eNcRiJX3VET+6rSjD6XGJnTnp3q9RmKpAesivysC0loC6D+VXpjE8DP1
m3kOhe7fPsuCnd7cyU0CgYEAm7cgSFoW0uWpVgjsrFpdmJCurYII9LtW1+1DK8sg
Z2edgL+Hocto09BfpbZ4AtrPxdMBvuSvT4RhBUTSfDWRY0Yj/A2/h1ZF6CQTInYX
FIGwJn+xg57t81oK941de9VhbfpUnR3BLPAropYU7BrYz2MTXngga61n2lXC8EmK
fyECgYB+WaDFNZmAH8FRRE8Pxk6dM7egIK9ExclsJ71V+cmE3DTzBWy21CD7Dkgt
rRVDSj1NaoOjFXBdWgTqjRZYDUay6B0jFF1WrSUg+cOfiq6NEj645F4QZVz7k7LZ
38/Dy1DTW19x01/wCvQ9O4XqZsmURzith6QA0imZF8IBpUz9Cw==
-----END RSA PRIVATE KEY-----"


ENCRYPTED_MESSAGE="4703fb71f9ff7d6c35d43095d06adcf86483d6cf61f95e761eaf4c717e1f6b0dd7d5449c04a394c1d0b8a9661aa96cbb4e581342fb05104ba4f44b424c29d4ed6b3da98abf2f5ff91bf413be6eab96e1167c2c00e0177a2e464d8a5e7fd1d27e7492571d7bb93db6405b9e4e3ef1a6c7c75b8eb38803ce3d30ee87f4481c27a83e85d887ffe6334043dc003a442aaa200e96e4d0423cca4c27fc1e73beec800017412e3a16951eebe21829679664c6f3ea001fd9c0862f6c72ee90d0c300f7e3f01f58eae6841bf035ddf071de7193d98df3c98e99f46bba93b48246fb111580b7c162c793035221b235aab2089f3c9f106b315a5fd5db9159e00cdbfcf6b10f"
# Replace ... with the actual encrypted message in hexadecimal form
# Escape the RSA private key for JSON
ESCAPED_RSA_PRIVATE_KEY=$(echo "$RSA_PRIVATE_KEY" | sed ':a;N;$!ba;s/\n/\\n/g')

# Create a JSON payload with both the private key and encrypted message
JSON_PAYLOAD="{\"private_key\": \"$ESCAPED_RSA_PRIVATE_KEY\", \"encrypted_message\": \"$ENCRYPTED_MESSAGE\"}"

# Send the JSON payload to the Flask app using curl
curl -X POST -H "Content-Type: application/json" -d "$JSON_PAYLOAD" https://ramraj13.pythonanywhere.com/process_data
