#Builds the user interface elements 
"""
UI Components for the Algorithm Visualizer
"""

import pygame
from constants import *


class Button:
    """A modern clickable button with hover effects and shadows"""
    
    BORDER_RADIUS = 10
    HOVER_BRIGHTNESS = 30
    SHADOW_OFFSET = 2
    
    def __init__(self, x, y, width, height, text, color, text_color=BUTTON_TEXT):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.base_color = color
        self.text_color = text_color
        self.hovered = False
        
    def draw(self, screen, font):
        """Draw the button with modern shadow and hover effect"""
        # Draw shadow
        shadow_rect = self.rect.copy()
        shadow_rect.x += self.SHADOW_OFFSET
        shadow_rect.y += self.SHADOW_OFFSET
        pygame.draw.rect(screen, (180, 180, 180), shadow_rect, border_radius=self.BORDER_RADIUS)
        
        # Draw button
        color = self._get_hover_color() if self.hovered else self.base_color
        pygame.draw.rect(screen, color, self.rect, border_radius=self.BORDER_RADIUS)
        
        # Draw border
        border_color = WHITE if not self.hovered else color
        pygame.draw.rect(screen, border_color, self.rect, 2, border_radius=self.BORDER_RADIUS)
        
        # Draw text
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def _get_hover_color(self):
        """Calculate lighter color for hover state"""
        return tuple(min(c + self.HOVER_BRIGHTNESS, 255) for c in self.base_color)
    
    def is_clicked(self, pos):
        """Check if button was clicked"""
        return self.rect.collidepoint(pos)
    
    def update_hover(self, pos):
        """Update hover state"""
        self.hovered = self.rect.collidepoint(pos)


class Dropdown:
    """A dropdown menu for selecting options"""
    
    BORDER_RADIUS = 8
    BORDER_WIDTH = 2
    ARROW_SIZE = 5
    TEXT_PADDING = 15
    
    def __init__(self, x, y, width, height, options, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.options = options
        self.selected = 0
        self.expanded = False
        self.font = font
        self.option_rects = []
        self.hovered_option = -1
        
    def draw(self, screen):
        """Draw the dropdown menu"""
        pygame.draw.rect(screen, DROPDOWN_BG, self.rect, border_radius=self.BORDER_RADIUS)
        pygame.draw.rect(screen, WHITE, self.rect, self.BORDER_WIDTH, border_radius=self.BORDER_RADIUS)
        
        # Draw selected option text
        text_surf = self.font.render(self.options[self.selected], True, TEXT_COLOR)
        text_rect = text_surf.get_rect(midleft=(self.rect.x + self.TEXT_PADDING, self.rect.centery))
        screen.blit(text_surf, text_rect)
        
        # Draw arrow
        self._draw_arrow(screen)
    
    def _draw_arrow(self, screen):
        """Draw dropdown arrow indicator"""
        arrow_x = self.rect.right - 20
        arrow_y = self.rect.centery
        
        if not self.expanded:
            # Down arrow
            points = [
                (arrow_x - self.ARROW_SIZE, arrow_y - 3),
                (arrow_x + self.ARROW_SIZE, arrow_y - 3),
                (arrow_x, arrow_y + 4)
            ]
        else:
            # Up arrow
            points = [
                (arrow_x - self.ARROW_SIZE, arrow_y + 3),
                (arrow_x + self.ARROW_SIZE, arrow_y + 3),
                (arrow_x, arrow_y - 4)
            ]
        pygame.draw.polygon(screen, TEXT_COLOR, points)
    
    def draw_expanded_options(self, screen):
        """Draw expanded options (should be called last to render on top)"""
        if not self.expanded:
            return
        
        screen_height = screen.get_height()
        total_height = len(self.options) * self.rect.height
        draw_upward = self.rect.bottom + total_height > screen_height
        
        self.option_rects = []
        for i, option in enumerate(self.options):
            option_y = self._calculate_option_y(i, draw_upward)
            option_rect = pygame.Rect(self.rect.x, option_y, self.rect.width, self.rect.height)
            self.option_rects.append(option_rect)
            
            self._draw_option(screen, option, option_rect, i)
    
    def _calculate_option_y(self, index, draw_upward):
        """Calculate Y position for an option"""
        if draw_upward:
            return self.rect.y - (len(self.options) - index) * self.rect.height
        else:
            return self.rect.y + (index + 1) * self.rect.height
    
    def _draw_option(self, screen, text, rect, index):
        """Draw a single option"""
        color = self._get_option_color(index)
        pygame.draw.rect(screen, color, rect, border_radius=self.BORDER_RADIUS)
        pygame.draw.rect(screen, WHITE, rect, self.BORDER_WIDTH, border_radius=self.BORDER_RADIUS)
        
        text_surf = self.font.render(text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(midleft=(rect.x + self.TEXT_PADDING, rect.centery))
        screen.blit(text_surf, text_rect)
    
    def _get_option_color(self, index):
        """Get color for an option based on hover and selection state"""
        if index == self.hovered_option:
            return DROPDOWN_HOVER
        elif index == self.selected:
            return GRAY
        else:
            return DROPDOWN_BG
    
    def handle_click(self, pos):
        """Handle click events on the dropdown"""
        if self.rect.collidepoint(pos):
            self.expanded = not self.expanded
            return True
        
        if self.expanded:
            for i, rect in enumerate(self.option_rects):
                if rect.collidepoint(pos):
                    self.selected = i
                    self.expanded = False
                    return True
        
        if self.expanded:
            self.expanded = False
        return False
    
    def update_hover(self, pos):
        """Update which option is being hovered"""
        self.hovered_option = -1
        if self.expanded:
            for i, rect in enumerate(self.option_rects):
                if rect.collidepoint(pos):
                    self.hovered_option = i
                    break


class Label:
    """A text label for displaying information"""
    
    def __init__(self, x, y, text, font, color=BLACK):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.color = color
        
    def draw(self, screen):
        """Draw the label"""
        text_surf = self.font.render(self.text, True, self.color)
        screen.blit(text_surf, (self.x, self.y))
        
    def update_text(self, text):
        """Update the label text"""
        self.text = text