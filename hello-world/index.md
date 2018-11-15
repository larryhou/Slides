% Awsome Book
% LARRY HOU
% Nov 15, 2018

## 第一章

### 1.1
- 1.1.1

```python
class SlideTransition(enum.Enum):
    none, fade, slide, convex, concave, zoom = range(6)

    @classmethod
    def option_choices(cls):
        choices = []
        for name, value in vars(cls).items():
            if isinstance(value, SlideTransition): choices.append(name)
        return choices

class SlideTheme(enum.Enum):
    black, white, league, beige, sky, night, serif, simple, solarized = range(9)

    @classmethod
    def option_choices(cls):
        choices = []
        for name, value in vars(cls).items():
            if isinstance(value, SlideTheme): choices.append(name)
        return choices

```

- 1.1.2

### 1.2

### 1.3

### 

## 第二章

### 2.1

### 2.2

### 3.3

## 第三章

