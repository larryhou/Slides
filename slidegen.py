#!/usr/bin/env python3

import enum, os, re

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

if __name__ == '__main__':
    import argparse, sys
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--transition', '-t', default='convex', choices=SlideTransition.option_choices(), help='slide transition')
    arguments.add_argument('--theme', '-m', default='white', choices=SlideTheme.option_choices(), help='slide theme')
    arguments.add_argument('--aspect', '-s', default='43', choices=['1610', '169', '149', '54', '43', '32'], help='1610=16:10 169=16:9 14:9=14:9 54=5:4 43=4:3 32=3:2')
    arguments.add_argument('--name', '-n', required=True, help='slide name')
    # reveal.js parameters
    arguments.add_argument('--var-controls', choices=['true', 'false'])
    arguments.add_argument('--var-controls-tutorial', choices=['true', 'false'])
    arguments.add_argument('--var-controls-layout')
    arguments.add_argument('--var-controls-back-arrows')
    arguments.add_argument('--var-progress', choices=['true', 'false'])
    arguments.add_argument('--var-slide-number', choices=['true', 'false'])
    arguments.add_argument('--var-history', choices=['true', 'false'])
    arguments.add_argument('--var-keyboard', choices=['true', 'false'])
    arguments.add_argument('--var-overview', choices=['true', 'false'])
    arguments.add_argument('--var-center', choices=['true', 'false'])
    arguments.add_argument('--var-touch', choices=['true', 'false'])
    arguments.add_argument('--var-loop', choices=['true', 'false'])
    arguments.add_argument('--var-rtl', choices=['true', 'false'])
    arguments.add_argument('--var-shuffle', choices=['true', 'false'])
    arguments.add_argument('--var-fragments', choices=['true', 'false'])
    arguments.add_argument('--var-fragment-in-url', choices=['true', 'false'])
    arguments.add_argument('--var-embedded', choices=['true', 'false'])
    arguments.add_argument('--var-help', choices=['true', 'false'])
    arguments.add_argument('--var-show-notes', choices=['true', 'false'])
    arguments.add_argument('--var-auto-play-media')
    arguments.add_argument('--var-auto-slide', type=int)
    arguments.add_argument('--var-auto-slide-stoppable', choices=['true', 'false'])
    arguments.add_argument('--var-auto-slide-method')
    arguments.add_argument('--var-default-timing', type=int)
    arguments.add_argument('--var-mouse-wheel', choices=['true', 'false'])
    arguments.add_argument('--var-hide-address-bar', choices=['true', 'false'])
    arguments.add_argument('--var-preview-links', choices=['true', 'false'])
    arguments.add_argument('--var-transition')
    arguments.add_argument('--var-transition-speed')
    arguments.add_argument('--var-background-transition')
    arguments.add_argument('--var-view-distance', type=int)
    arguments.add_argument('--var-parallax-background-image')
    arguments.add_argument('--var-parallax-background-size')
    arguments.add_argument('--var-parallax-background-horizontal')
    arguments.add_argument('--var-parallax-background-vertical')
    arguments.add_argument('--var-display')

    default_options = {'controls': ['controls', 'true'], 'controls_tutorial': ['controlsTutorial', 'true'], 'controls_layout': ['controlsLayout', 'bottom-right'], 'controls_back_arrows': ['controlsBackArrows', 'faded'], 'progress': ['progress', 'true'], 'slide_number': ['slideNumber', 'false'], 'history': ['history', 'false'], 'keyboard': ['keyboard', 'true'], 'overview': ['overview', 'true'], 'center': ['center', 'true'], 'touch': ['touch', 'true'], 'loop': ['loop', 'false'], 'rtl': ['rtl', 'false'], 'shuffle': ['shuffle', 'false'], 'fragments': ['fragments', 'true'], 'fragment_in_url': ['fragmentInURL', 'false'], 'embedded': ['embedded', 'false'], 'help': ['help', 'true'], 'show_notes': ['showNotes', 'false'], 'auto_play_media': ['autoPlayMedia', None], 'auto_slide': ['autoSlide', 0], 'auto_slide_stoppable': ['autoSlideStoppable', 'true'], 'auto_slide_method': ['autoSlideMethod', 'Reveal.navigateNext'], 'default_timing': ['defaultTiming', 120], 'mouse_wheel': ['mouseWheel', 'false'], 'hide_address_bar': ['hideAddressBar', 'true'], 'preview_links': ['previewLinks', 'false'], 'transition': ['transition', 'slide'], 'transition_speed': ['transitionSpeed', 'default'], 'background_transition': ['backgroundTransition', 'fade'], 'view_distance': ['viewDistance', 3], 'parallax_background_image': ['parallaxBackgroundImage', ''], 'parallax_background_size': ['parallaxBackgroundSize', ''], 'parallax_background_horizontal': ['parallaxBackgroundHorizontal', None], 'parallax_background_vertical': ['parallaxBackgroundVertical', None], 'display': ['display', 'block']}

    options = arguments.parse_args(sys.argv[1:])
    import os.path as p
    os.chdir(p.dirname(p.abspath(__file__)))
    slide_name = options.name
    assert p.isdir(p.join(os.getcwd(), slide_name))
    config = {
        'revealjs-url': '../reveal.js',
        'theme': options.theme,
        'aspectratio': options.aspect,
        'transition': options.transition
    }

    for name, value in vars(options).items():
        if name.startswith('var_') and value:
            name = re.sub(r'^var_', '', name)
            assert name in default_options, name
            item = default_options.get(name)
            config[item[0]] = value

    command = 'pandoc -s --mathjax -i -t revealjs'
    for name, value in config.items():
        command += ' --variable {}={!r}'.format(name, ('true' if value else 'false') if isinstance(value, bool) else value)

    command += ' {}/index.md'.format(slide_name)
    command += ' -o {}/index.html'.format(slide_name)
    print('+ {}'.format(command))
    assert os.system(command) == 0



