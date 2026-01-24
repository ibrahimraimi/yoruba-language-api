# Stage 1: Build WWW
FROM oven/bun:1 AS builder-www
WORKDIR /app
COPY www/package.json www/bun.lock* ./
RUN bun install
COPY www/ ./
RUN bun run build

# Stage 2: Build Docs
FROM oven/bun:1 AS builder-docs
WORKDIR /app
COPY docs/package.json docs/bun.lock* ./
RUN bun install --ignore-scripts
COPY docs/ ./
RUN bun run postinstall
RUN bun run build

# Stage 3: Final image
FROM node:20-alpine
RUN apk add --no-cache nginx libc6-compat

WORKDIR /app

# Setup WWW
COPY --from=builder-www /app/.next/standalone ./www
COPY --from=builder-www /app/.next/static ./www/.next/static
COPY --from=builder-www /app/public ./www/public

# Setup Docs
COPY --from=builder-docs /app/.next/standalone ./docs
COPY --from=builder-docs /app/.next/static ./docs/.next/static

# Copy Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
