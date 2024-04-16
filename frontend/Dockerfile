# ---- Node modules ----- #
FROM oven/bun AS node_modules

WORKDIR /opt/app

COPY ./package*.json ./bun* ./

RUN bun install --ignore-scripts

# ---- Build ------------ #
FROM node:20.9.0-bullseye-slim AS dist

WORKDIR /opt/app

COPY --from=node_modules /opt/app/node_modules ./node_modules
COPY ./ .

RUN npm run lint
RUN npm run build

# ---- Release ---------- #
FROM gcr.io/distroless/nodejs20-debian12

WORKDIR /opt/app

COPY --from=dist /opt/app/.nuxt .nuxt
COPY --from=dist /opt/app/.output .output

ENV HOST 0.0.0.0
CMD [ "./.output/server/index.mjs" ]
