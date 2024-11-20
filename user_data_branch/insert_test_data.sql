-- Insert mock data into users table
INSERT OR IGNORE INTO users (id, name, age, weight, height, goal) VALUES
(1, 'Alice', 25, 65.0, 165, 'muscle gain'),
(2, 'Bob', 30, 80.0, 175, 'weight loss'),
(3, 'Charlie', 35, 75.0, 180, 'maintenance'),
(4, 'Dana', 28, 60.0, 160, 'endurance'),
(5, 'Evan', 40, 90.0, 170, 'muscle gain');

-- Insert mock data into user_goals table
INSERT OR IGNORE INTO user_goals (id, user_id, goal, calories, protein, carbs, fats, vitamin_c, calcium, iron) VALUES
(1, 1, 'muscle gain', 3000, 150, 350, 100, 90, 1000, 18),
(2, 2, 'weight loss', 2000, 100, 200, 70, 75, 800, 15),
(3, 3, 'maintenance', 2500, 120, 250, 80, 80, 900, 16),
(4, 4, 'endurance', 2800, 130, 300, 90, 85, 950, 17),
(5, 5, 'muscle gain', 3200, 160, 360, 110, 100, 1200, 20);
