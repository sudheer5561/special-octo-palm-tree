from reverse_figlet import render


def test_rendered_text_is_in_big_enough_font():
    rendered = render('Short one')
    assert len(rendered.split('\n')) > 3
