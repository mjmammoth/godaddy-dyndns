# Quick and Dirty GoDaddy DynDNS Updater
#### Supports multiple subdomains of a single domain

All configuration is managed through environment variables

| Environment Variable     | Description |
| ----------- | ----------- |
| GODADDY_ KEY     | API key obtained through the [GoDaddy Developer Page](https://developer.godaddy.com/keys)       |
| GODADDY_SECRET   | Generated alongside the key in the above step        |
|DOMAIN|The base domain you have control over|
|SUBDOMAINS| Every subdomain of the base domain separated by a semicolon `;`|

## Docker-Compose Example
```
---
version: "2.1"
services:
  godaddy-dyndns:
    image: mjmammoth/godaddy-dyndns:latest
    container_name: godaddy-dns
    env_file:
      - .env
    restart: unless-stopped
```

Where `.env` file contains something like;
```
DOMAIN=example.com
SUBDOMAINS=foo;bar;baz
GODADDY_KEY=12345678_aBcDeFgHiJkLmNoP
GODADDY_SECRET=AbCdEf1234567
```
