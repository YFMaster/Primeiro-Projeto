# Primeiro-Projeto
# MyDjangoApp

## Visão Geral

### Sobre o aplicativo

**MyDjangoApp** é uma **plataforma web responsiva (focada em desktop/PC)** que coleta em tempo real os editais e notícias do site **PCI Concursos** e apresenta de forma filtrável todas as oportunidades de concursos públicos abertos no Brasil.

Recursos principais:

* **Raspagem programada**: tarefas Celery/Beat buscam novos editais a cada 6 h.
* **Filtro avançado**: por órgão, cargo, nível de escolaridade, remuneração, estado e data‑limite de inscrição.
* **Favoritos & alertas**: usuários autenticados podem salvar concursos e receber e‑mails quando houver retificação ou novas vagas semelhantes.
* **Exportação**: gera PDF ou planilha Excel com concursos filtrados.
* **Design desktop‑first**: layout fluido em 1440 px levando em conta telas de trabalho, mas ainda mobile‑friendly via Tailwind.

> A ideia é simplificar a vida de quem estuda para concursos, reunindo todas as informações num só lugar, sem depender de múltiplos sites e RSS.

> **MyDjangoApp** é um esqueleto de aplicação web moderna construída com **Django 5.2 LTS** que serve como ponto de partida para projetos de pequeno, médio ou grande porte. O objetivo é oferecer um ambiente de desenvolvimento produtivo, seguro e pronto para deploy em containers.

Este README descreve todas as etapas e ferramentas recomendadas para configurar, desenvolver, testar e publicar o projeto.

---

## Stack Principal

| Camada                          | Ferramentas & Tecnologias                                                             | Motivo da escolha                                          |
| ------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Linguagem**                   | Python 3.12 +                                                                         | Última versão estável suportada pelo Django 5.2            |
| **Framework Web**               | Django 5.2 LTS                                                                        | Confiável, segurança embutida, ciclo de suporte prolongado |
| **Banco de Dados**              | PostgreSQL 16                                                                         | Consistência ACID, JSONB, ótimo suporte oficial            |
| **Cache/Filas**                 | Redis 7 (+ Celery 5 / django‑celery‑beat)                                             | Cache & tarefas assíncronas                                |
| **Frontend**                    | Django Template Language + HTMX + Alpine.js + Tailwind CSS (ou React + Vite opcional) | Curva de aprendizado suave / SPA opcional                  |
| **Container**                   | Docker 25 + Docker Compose                                                            | Paridade dev‑prod                                          |
| **Gerenciador de dependências** | Poetry 1.8 (ou Pipenv)                                                                | Lockfile reprodutível                                      |
| **Testes**                      | pytest‑django + factory\_boy + coverage                                               | Suíte de testes rápida e expressiva                        |
| **Qualidade de código**         | pre‑commit (black, isort, flake8, mypy, ruff, bandit)                                 | Padrão de código consistente                               |
| **CI/CD**                       | GitHub Actions                                                                        | Testes, lint e build automáticos                           |

---

## Pré‑requisitos

* Git
* Docker e Docker Compose plugin
* Make (Linux/macOS) ou GNU Make for Windows
* (Opcional) Python >= 3.12 e Poetry caso não utilize Docker
* (Opcional) Node.js >= 20 se for usar assets JS/React

---

## Estrutura de Pastas

```
mydjangoapp/
├── compose/             # arquivos docker-compose (dev e prod)
│   ├── development.yml
│   └── production.yml
├── config/              # configuração do projeto
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── apps/                # aplicativos internos reutilizáveis
│   ├── core/
│   └── users/
├── static/              # assets compilados (JS/CSS/Imgs)
├── templates/           # templates HTML (Jinja/DjangoTPL)
├── tests/               # testes automatizados
├── manage.py
├── Makefile
├── pyproject.toml       # Poetry config (dependências)
└── README.md
```

---

## Configuração Rápida (Docker)

```bash
# 1. Clone o repositório
$ git clone https://github.com/seu-usuario/mydjangoapp.git
$ cd mydjangoapp

# 2. Instale os hooks do pre-commit
$ pre-commit install

# 3. Copie variáveis de ambiente
$ cp .env.example .env

# 4. Build + up
$ docker compose -f compose/development.yml build
$ docker compose -f compose/development.yml up -d

# 5. Migrações e usuário admin
$ docker compose exec web python manage.py migrate
$ docker compose exec web python manage.py createsuperuser

# 6. Acesse
Abra http://localhost:8000 🇧🇷
```

### Sem Docker

1. Instale Python 3.12 + e Poetry
2. `poetry install`
3. `pre-commit install`
4. Configure PostgreSQL e crie banco `mydjangoapp`
5. `cp .env.example .env`
6. `python manage.py migrate && python manage.py runserver`

---

## Principais Comandos (Makefile)

| Comando       | Descrição                           |
| ------------- | ----------------------------------- |
| `make up`     | Sobe containers em modo detach      |
| `make down`   | Derruba containers                  |
| `make bash`   | Shell interativo no container `web` |
| `make logs`   | Logs unificados                     |
| `make test`   | Executa suíte de testes             |
| `make lint`   | Roda linters/formatadores           |
| `make format` | Aplica black + isort                |

---

## Fluxo de Desenvolvimento

1. Crie branch a partir de `main` (`git checkout -b feature/descrição`)
2. Instale hooks: `pre-commit install`
3. Escreva código **+** testes
4. Commit (`git commit -m "feat: ..."`)
5. Push & abra Pull Request no GitHub
6. GitHub Actions garante que testes e lint passem
7. Merge via *Squash* / *Rebase* para manter histórico limpo

---

## Deploy

### Railway / Render / Fly.io

```bash
# Build & deploy (exemplo Railway)
railway link
railway run migrate
railway up
```

* Defina variáveis de ambiente no dashboard
* Serviço web: `gunicorn config.wsgi:application --log-file -`
* Serviço worker: `celery -A config worker -l info`
* Configure autoscale e domínio customizado

### VPS (Ubuntu 22.04 + Docker)

1. Instale Docker & Docker Compose
2. `git clone` → `.env` → `docker compose -f compose/production.yml up -d`
3. Configure proxy reverso (Nginx ou Caddy) e TLS (LetsEncrypt)

### Escalabilidade

* Use múltiplas réplicas Gunicorn atrás de Nginx/Traefik
* Habilite cachê Redis + CDN (Cloudflare) para assets
* Sharding ou réplica PostgreSQL quando necessário

---

## Testes & Qualidade

```bash
pytest -q                          # roda testes
coverage run -m pytest && coverage html
ruff check .                       # lint ultra‑rápido
bandit -r apps/                    # segurança estática
```

---

## Segurança & Boas Práticas

* **Segredos**: mantenha em variáveis de ambiente (`django-environ`)
* **HTTPS**: ative `SECURE_SSL_REDIRECT`, cookies `secure`
* **CORS**: use `django-cors-headers` se front separado
* **CSRF**: habilitado por padrão; use tokens ao consumir API
* **Headers**: `django-secure`, `django-feature-policy`
* **Dependabot**: habilite no GitHub para updates de segurança

---

## Extensões Futuras

* API RESTful → **Django REST Framework**
* Autenticação social → **django‑allauth**
* WebSockets → **Django Channels**
  \* Admin customizado → **django‑jazzmin**
* Internacionalização (i18n) pronta 🇧🇷/🇺🇸

---

## Contribuindo

1. Abra uma *issue* descrevendo a feature/bug
2. Vincule PR à issue
3. Siga convenção de commits [Conventional Commits](https://www.conventionalcommits.org/)
4. Atualize o README se necessário
5. Agradecemos sua contribuição!

---

## Licença

Distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para detalhes.

---

## Autor

**Yan Faulhaber Maia** – [LinkedIn](https://www.linkedin.com/in/yan-faulhaber-43362b243/)


