# Stage 1: Build the application
# Using Node.js version 16 (or you can use 14 or higher)
FROM node:16 as build

# Create app directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install all dependencies
RUN npm install

# Copy the rest of your application's source code
COPY . .

# Build the application (uncomment if you have a build step in your package.json)
# RUN npm run build

# Stage 2: Setup production environment
FROM node:16 as production

# Set NODE_ENV environment variable
ENV NODE_ENV=production

# Create app directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install only production dependencies
RUN npm install --only=production

# Copy built assets from the build stage
COPY --from=build /usr/src/app/dist ./dist

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run your app
# (adjust this if your start script is different)
CMD ["node", "dist/main"]
