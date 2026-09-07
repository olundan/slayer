class Camera:
    def __init__(self, width: int, height: int, x: int = 0, y: int = 0):
        self.width = width   
        self.height = height 
        self.x = x           
        self.y = y           

    def follow(self, target_x: int, target_y: int):
        self.x = target_x - (self.width // 2)
        self.y = target_y - (self.height // 2)

    def draw_sprite(self, renderer, world_x: int, world_y: int, sprite):
        screen_x = world_x - self.x
        screen_y = world_y - self.y

        sprite_h = len(sprite.pattern)
        sprite_w = max((len(row) for row in sprite.pattern), default=0)

        if (screen_x + sprite_w <= 0 or screen_x >= self.width or
            screen_y + sprite_h <= 0 or screen_y >= self.height):
            return  

        crop_start_x = max(0, -screen_x)
        crop_start_y = max(0, -screen_y)
        crop_end_x = min(sprite_w, self.width - screen_x)
        crop_end_y = min(sprite_h, self.height - screen_y)

        visible_sprite = sprite.cropped(crop_start_x, crop_start_y, crop_end_x, crop_end_y)

        draw_x = max(0, screen_x)
        draw_y = max(0, screen_y)

        renderer.add_sprite(draw_x, draw_y, visible_sprite)
