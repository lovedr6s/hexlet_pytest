from hexlet_pytest.example import reverse, stacks

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_stacks():
    stack = stacks()
    assert stack.pop() == 3
    assert stack.pop() == 2