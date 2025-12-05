import pygame
import sys
import math

# Read input
with open('../day1.txt', 'r') as f:
    rotations = [line.strip() for line in f.readlines()]

# Parse rotations
parsed_rotations = []
for rotation in rotations:
    direction = rotation[0]
    distance = int(rotation[1:])
    parsed_rotations.append((direction, distance))

# Part 1: Count times dial ends at 0 after each rotation
def solve_part1(rotations):
    position = 50
    count = 0
    
    for direction, distance in rotations:
        if direction == 'L':
            position = (position - distance) % 100
        else:  # 'R'
            position = (position + distance) % 100
        
        if position == 0:
            count += 1
    
    return count

# Part 2: Count times dial passes through 0 (including during rotations)
def solve_part2(rotations):
    position = 50
    count = 0
    
    for direction, distance in rotations:
        if direction == 'L':
            # Count how many times we cross 0 going left
            for step in range(1, distance + 1):
                new_pos = (position - step) % 100
                if new_pos == 0:
                    count += 1
            position = (position - distance) % 100
        else:  # 'R'
            # Count how many times we cross 0 going right
            for step in range(1, distance + 1):
                new_pos = (position + step) % 100
                if new_pos == 0:
                    count += 1
            position = (position + distance) % 100
    
    return count

# Calculate answers
part1_answer = solve_part1(parsed_rotations)
part2_answer = solve_part2(parsed_rotations)

print(f"Part 1: {part1_answer}")
print(f"Part 2: {part2_answer}")

# Visualization with pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 120
DIAL_CENTER = (WIDTH // 2, HEIGHT // 2)
DIAL_RADIUS = 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Safe Dial Rotation")
clock = pygame.time.Clock()

font_large = pygame.font.Font(None, 48)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# Visualization state
current_rotation_idx = 0
rotation_progress = 0.0  # 0 to 1
position = 50
count_part1 = 0
count_part2 = 0
times_crossed_zero_this_rotation = 0
is_paused = False

def draw_dial():
    """Draw the safe dial"""
    # Draw outer circle
    pygame.draw.circle(screen, (100, 100, 100), DIAL_CENTER, DIAL_RADIUS, 3)
    
    # Draw numbers 0-99 around the dial
    for i in range(100):
        angle = math.radians((i * 360 / 100) - 90)  # Start from top
        x = DIAL_CENTER[0] + DIAL_RADIUS * math.cos(angle)
        y = DIAL_CENTER[1] + DIAL_RADIUS * math.sin(angle)
        
        # Highlight every 10th number
        if i % 10 == 0:
            pygame.draw.circle(screen, (255, 255, 0), (int(x), int(y)), 6)
            text = font_small.render(str(i), True, (0, 0, 0))
            text_rect = text.get_rect(center=(int(x), int(y)))
            screen.blit(text, text_rect)
        else:
            pygame.draw.circle(screen, (150, 150, 150), (int(x), int(y)), 2)

def draw_pointer():
    """Draw the arrow pointer at top"""
    pointer_length = DIAL_RADIUS + 30
    angle = math.radians((position * 360 / 100) - 90)
    
    x = DIAL_CENTER[0] + pointer_length * math.cos(angle)
    y = DIAL_CENTER[1] + pointer_length * math.sin(angle)
    
    # Draw arrow line
    pygame.draw.line(screen, (255, 0, 0), DIAL_CENTER, (int(x), int(y)), 4)
    
    # Draw arrow head
    arrow_size = 15
    angle1 = angle + math.radians(150)
    angle2 = angle - math.radians(150)
    
    p1 = (int(x + arrow_size * math.cos(angle1)), int(y + arrow_size * math.sin(angle1)))
    p2 = (int(x + arrow_size * math.cos(angle2)), int(y + arrow_size * math.sin(angle2)))
    pygame.draw.polygon(screen, (255, 0, 0), [p1, (int(x), int(y)), p2])
    
    # Highlight 0 in green
    if position == 0:
        pygame.draw.circle(screen, (0, 255, 0), DIAL_CENTER, 20, 4)

def draw_info():
    """Draw info text"""
    if current_rotation_idx < len(parsed_rotations):
        direction, distance = parsed_rotations[current_rotation_idx]
        rotation_text = f"Rotation {current_rotation_idx + 1}/{len(parsed_rotations)}: {direction}{distance}"
    else:
        rotation_text = "All rotations complete!"
    
    text = font_medium.render(rotation_text, True, (255, 255, 255))
    screen.blit(text, (20, 20))
    
    position_text = font_medium.render(f"Position: {position}", True, (255, 255, 255))
    screen.blit(position_text, (20, 70))
    
    count_text1 = font_small.render(f"Part 1 (ends at 0): {count_part1}", True, (255, 255, 0))
    screen.blit(count_text1, (20, 120))
    
    count_text2 = font_small.render(f"Part 2 (passes through 0): {count_part2}", True, (0, 255, 255))
    screen.blit(count_text2, (20, 150))
    
    crossed_text = font_small.render(f"Crossed 0 this rotation: {times_crossed_zero_this_rotation}", True, (0, 255, 0))
    screen.blit(crossed_text, (20, 180))
    
    pause_text = font_small.render("SPACE to pause/resume, Q to quit", True, (200, 200, 200))
    screen.blit(pause_text, (20, HEIGHT - 40))

# Main visualization loop
running = True
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_SPACE:
                is_paused = not is_paused
    
    if not is_paused and current_rotation_idx < len(parsed_rotations):
        rotation_progress += 1 / (0.05 * FPS)  # 0.05 seconds per rotation
        
        if rotation_progress >= 1.0:
            rotation_progress = 0.0
            current_rotation_idx += 1
            times_crossed_zero_this_rotation = 0
    
    # Update position based on progress
    if current_rotation_idx < len(parsed_rotations):
        direction, distance = parsed_rotations[current_rotation_idx]
        
        if direction == 'L':
            current_pos = (50 + (current_rotation_idx - 1) * 0 - (rotation_progress * distance)) % 100
        else:  # 'R'
            current_pos = (50 + (current_rotation_idx - 1) * 0 + (rotation_progress * distance)) % 100
        
        # Recalculate from scratch to get accurate position
        temp_pos = 50
        for i in range(current_rotation_idx):
            d, dist = parsed_rotations[i]
            if d == 'L':
                temp_pos = (temp_pos - dist) % 100
            else:
                temp_pos = (temp_pos + dist) % 100
        
        # Apply current rotation progress
        d, dist = parsed_rotations[current_rotation_idx]
        if d == 'L':
            position = (temp_pos - (rotation_progress * dist)) % 100
        else:
            position = (temp_pos + (rotation_progress * dist)) % 100
        
        # Count crossings through 0
        times_crossed_zero_this_rotation = 0
        d, dist = parsed_rotations[current_rotation_idx]
        if d == 'L':
            for step in range(1, int(rotation_progress * dist) + 1):
                if ((temp_pos - step) % 100) == 0:
                    times_crossed_zero_this_rotation += 1
        else:
            for step in range(1, int(rotation_progress * dist) + 1):
                if ((temp_pos + step) % 100) == 0:
                    times_crossed_zero_this_rotation += 1
    
    # Calculate totals at current point
    count_part1 = 0
    count_part2 = 0
    temp_pos = 50
    
    for i in range(current_rotation_idx):
        d, dist = parsed_rotations[i]
        if d == 'L':
            for step in range(1, dist + 1):
                if ((temp_pos - step) % 100) == 0:
                    count_part2 += 1
            temp_pos = (temp_pos - dist) % 100
        else:
            for step in range(1, dist + 1):
                if ((temp_pos + step) % 100) == 0:
                    count_part2 += 1
            temp_pos = (temp_pos + dist) % 100
        
        if temp_pos == 0:
            count_part1 += 1
    
    # If currently animating, count crossings so far
    if current_rotation_idx < len(parsed_rotations):
        d, dist = parsed_rotations[current_rotation_idx]
        steps = int(rotation_progress * dist)
        if d == 'L':
            for step in range(1, steps + 1):
                if ((temp_pos - step) % 100) == 0:
                    count_part2 += 1
        else:
            for step in range(1, steps + 1):
                if ((temp_pos + step) % 100) == 0:
                    count_part2 += 1
    
    # Draw
    screen.fill((20, 20, 40))
    draw_dial()
    draw_pointer()
    draw_info()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
