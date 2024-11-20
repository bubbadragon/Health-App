CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    weight REAL,
    height REAL,
    goal TEXT
);

CREATE TABLE IF NOT EXISTS user_goals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    goal TEXT,
    calories INTEGER,
    protein INTEGER,
    carbs INTEGER,
    fats INTEGER,
    vitamin_c INTEGER,
    calcium INTEGER,
    iron INTEGER,
    -- Add more nutrients as needed
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS workout_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATETIME NOT NULL,
    workout_name VARCHAR(255) NOT NULL,
    duration VARCHAR(50),
    exercise_name VARCHAR(255) NOT NULL,
    set_order INTEGER,
    weight REAL,
    reps INTEGER,
    distance REAL,
    seconds INTEGER,
    notes TEXT,
    workout_notes TEXT,
    rpe INTEGER
);

