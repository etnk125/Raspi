# getting start
1. create gg cloud platform instance
2. apply api
   - gg sheet
   - gg drive
3. create credential as json
4. create gg sheet and add editor mail from credential file
   
## install 

```cmd
sudo pip3 install gspread
sudo pip3 install --upgrade oauth2client
```

## credential example:

```json
{
  "type": "service_account",
  "project_id": "triple-carrier-345610",
  "private_key_id": "508336cf27b1165e8a84e8c1bda36fdef27d7a42",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvYiuJm7Fli/p1\ny5rhbpCidyzc3aoX8MCpjhZaYHweEAZOcZTSbHBCgugHDd6h1dnwQvIjOykCGC/l\nVtij0tiXc1cMCuSA9x4UFJnOsbvkjdnYlJ6ppl4Pe4SeKGziPcnJ7hdZLo3Ft6se\nYEasklEiwdoZcuFlIiO0sa4FQvUhv5UZeFNIO4aJY/QBk7frk0pHcyb34ESvbl1h\nVkhTPq8KYWoe7yQgjsor5HiaQMxxeXX8xjgZZE6Q3tx45TQgEnBax3WYClnNrhaK\ndzQnJUuN6YmSc57lBaEHs9P3OnfI80PG8/3GL7JCVX3ZcdKevoiIknXVfMnhLyw9\n4cqPODCXAgMBAAECggEADMD7qoj0bbkwBa3rPZaFP732jg8z5dl09pTlwj0UTuQF\nGWJAG3dASKNCt/SbFTNlzbIzRTrxoKcyoHUK0bWtA4J4jjXNPSWl/c7WX9tj7wXJ\nFZYP3bAX/1HmUyaxwwK8RbTMj4iHox0CqCBXM13RNvutiRPmGS0njJCD4k+8Chqe\nHDRhiWgrV6ix9rTywuu/LS1sJ+FUVome9xdMMDJdmdmTVoNt+h5g/5Q3V30AnLgy\np6qqFlNR6/1dbZUflqskNMHnZePL/oX1NOm3FbAdE7UvurBcdjiezqTRQsupau0i\nS3oLmnOf9n9aTYaNelqQer2y+0UiiI2ZyLYAWPfxpQKBgQDijtoCcjeUdqoxPg3t\nSxZCn+kDmzTSAhjyoBfRDDhIlh/F8APedrp2Da7ZrS3KoFl3n9yoKqLLA2wlCQ8v\ncieTBBkRxcZB73XJmysBx6iYPqm1+iBWmY6peJmiX+xGxAPH7MLAEULzZcjvsHNJ\nAvgcOzUv6Bww9MzUXwabdzSZdQKBgQDGLNcbbVkpPUsU/WWk9hoP/k/dlkM+5v2e\nWvSJw9AGIV0Ww1R+IkbThBZvJNk0IKuSVH9lv5uDwDGr2JZ47mieqGdZ/laT4V+y\nlKpjKTb0TBfCDfnIspzBJhKP78LsD79aA7JAu543wo+Ao6ciCm1YNICWlUAguXRY\nxFdTo9aUWwKBgAlXNmnPZ7c5RT8OfeiApgRNL4A0j/LwnzKxowm9ZTyo49p3UNGF\nN57SZZkX6MFn5whlkOVmDJwuIfFM9FFSdYs8KgRvkQL66nJLcXR7VNoiC0EzdM3d\nOuKF1F+7cLRiNH2zpzvf+lCqq6QmNDqYYr5XOpQlD7R9A0zmNhGG0qZZAoGASPvq\nnKdA1vdD148bCA26u3klYK4eReQ8Mz28IaCD1D4lUmTNkUZ+XxeeS4B+nbwKc/G6\nmXZfh74YjPlPMWpcDVJn/bS1nfC6lcI6nhpnqsD7XvRWsZtWL6wd2fSrDNUf277Q\nvxZZxp9Yyj97JgZBDuMHGG4PF/404xwsLRmBxVECgYEA1psx0XLBrJzi826jKkuA\nE/RzwFrkYyuAR7T5+9blVsgYhzUYXS6yjlxdaE9GrBw8SJbmtkZbkbcRNryxSm8D\nZoareJq5YlpkRKyqTmhct9RAp8RUXlWoKkMLgSdPBRZSXAfYvtE6CcT64QHz7dJJ\nymFebycP8CHVXr5Vn8zoEzo=\n-----END PRIVATE KEY-----\n",
  "client_email": "sheet-331@triple-carrier-345610.iam.gserviceaccount.com",
  "client_id": "103621354017342437041",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sheet-331%40triple-carrier-345610.iam.gserviceaccount.com"
}

```
## command
1. Insert in specific line
  ```
  worksheet.insert_row(data,row)
  ```
2. Append data to the next row
  ```
  worksheet.append_row(data1,data2,…,dataN)
  ```
3. Update data
  ```
  worksheet.update_cell(row,col,data)
  ```
4. Read data
  ```
  x = worksheet.get_all_records()
  ```
5. Read data from cell
  ```
  x = worksheet.cell(row,col)
  ```
6. Delete data
  ```
  worksheet.delete_row(row)
  ```