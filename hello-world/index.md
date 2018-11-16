% Awsome Book
% LARRY HOU
% Nov 15, 2018

## 第一章

### 1.1
* 1.1.1

<div class="fragment">
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
    black, white, league, beige, sky, night, serif, simple, solarized, blood, moon = range(11)

    @classmethod
    def option_choices(cls):
        choices = []
        for name, value in vars(cls).items():
            if isinstance(value, SlideTheme): choices.append(name)
        return choices

```
</div>

* 1.1.2

### 1.2

### 1.3

### 

| | | | |
|:--|:--|:--|:--|
|8 bit| byte (int8)| ubyte (uint8)| bool|
|16 bit| short (int16)| ushort (uint16)||
|32 bit| int (int32)| uint (uint32)| float (float32)|
|64 bit| long (int64)| ulong (uint64)| double (float64)|

## 第二章

### 2.1

### 2.2

### 3.3

## 第三章

