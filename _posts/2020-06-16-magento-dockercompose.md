---
title: "Run Magento Local"
published: true
---

Hello this is my first blog post, hope you like it 😄.
I faced some problems trying to get magento running on my local device, so this post will go with you through setup steps, I didn't invent the solution just documenting it for future usage.

**This tutorial assumes you have docker and docker-compose**

First you will need to install the docker compose file from [bitnami](https://github.com/bitnami/bitnami-docker-magento).

``` bash
curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-magento/master/docker-compose.yml > docker-compose.yml
docker-compose up -d
```
You will probably need to change port 80 in the yml

``` yml
    ports:
      - '8080:80'
      - '8443:443'
```

If you want to access it via localhost not 127.0.0.1 add `MAGENTO_HOST`


``` yml
    magento:
      enviroment:
        - MAGENTO_HOST=localhost
```
After doing all of this you will face a problem in accessing admin panels, as the hosts doesn't really access the right port.

I came around [this](https://github.com/bitnami/bitnami-docker-magento/issues/85?fbclid=IwAR00q3aNQDTFw-Yi56cNi-nUZVeyI0QH_HuuH6KUqvf6tGLlvBNSz49BOeM#issuecomment-418826319) solution where I could fix the port problem from the DB.

First you will change the URLs from DB by

``` bash
docker-compose exec mariadb mysql -u 'root'
use bitnami_magento;
update core_config_data set value="https://localhost:8443/" where path='web/secure/base_url';
update core_config_data set value="http://localhost:8080/" where path='web/unsecure/base_url';
```
Then you will need to flush the cache via

``` bash
docker-compose exec magento bash
cd opt/bitnami/magento/htdocs/
bin/magento cache:flush
```
