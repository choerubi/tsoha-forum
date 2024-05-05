CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE forums (
    id SERIAL PRIMARY KEY,
    title TEXT,
    user_id INTEGER REFERENCES users,
    created_at TIMESTAMP,
    visible INTEGER
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    title TEXT,
    user_id INTEGER REFERENCES users,
    forum_id INTEGER REFERENCES forums,
    created_at TIMESTAMP
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    thread_id INTEGER REFERENCES threads,
    sent_at TIMESTAMP
);

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    message_id INTEGER REFERENCES messages
);