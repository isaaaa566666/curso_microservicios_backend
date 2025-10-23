\# Laboratorio de Microservicios (Django + React)



\## Arquitectura inicial

\- \*\*auth-service/\*\* → Servicio de autenticación y tokens JWT

\- \*\*blog-service/\*\* → Servicio de publicaciones y autores

\- \*\*email-service/\*\* → Servicio de notificaciones

\- \*\*frontend/\*\* → Interfaz React

\- \*\*reverse-proxy/\*\* → Gateway / balanceador local



\## Servicios base

\- PostgreSQL (puerto 5432)

\- Redis (puerto 6379)



\## Variables de entorno

Ver archivo `.env.example` para configuración base.



\## Comandos útiles

\- `docker compose up -d` → Levanta los contenedores  

\- `docker ps` → Verifica los contenedores activos  

\- `docker exec -it db\_postgres bash` → Entrar al contenedor de Postgres  

\- `docker logs <nombre\_contenedor>` → Ver logs de un contenedor  



---



✅ \*\*Checklist\*\*

\- \[x] Estructura de carpetas creada  

\- \[x] Docker Compose funcionando  

\- \[x] Variables de entorno definidas  

\- \[x] README documentado  



