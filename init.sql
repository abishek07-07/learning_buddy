-- 1. Enable the extension (once per database)
CREATE EXTENSION IF NOT EXISTS vector;

-- 2. Single table storing doc info + chunk + embedding
CREATE TABLE IF NOT EXISTS book_chunks (
    id           BIGSERIAL PRIMARY KEY,
    book_name    TEXT NOT NULL,
    author_name  TEXT NOT NULL,
    chunk_index  INT  NOT NULL,               -- order of chunk within the book
    content      TEXT NOT NULL,               -- the chunk text
    embedding    vector(1536) NOT NULL,       -- adjust dimension to your model
    metadata     JSONB DEFAULT '{}'::jsonb,   -- optional extras (chapter, page, etc.)
    created_at   TIMESTAMPTZ DEFAULT now(),
    UNIQUE (book_name, author_name, chunk_index)
);

-- 3. HNSW index for fast cosine similarity search
CREATE INDEX IF NOT EXISTS idx_book_chunks_embedding
    ON book_chunks
    USING hnsw (embedding vector_cosine_ops);