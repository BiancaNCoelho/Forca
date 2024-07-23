import pytest
import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from forca import mensagem, palavra_secreta, chute, inicializa_letras_acertadas, forca, adicionar_palavra

def test_mensagem(capsys):
    mensagem()
    captured = capsys.readouterr()
    assert captured.out.strip() == "JOGO DA FORCA!"

def test_palavra_secreta(tmpdir):
    testfile = tmpdir.join("lista.txt")
    testfile.write("python\njava\nruby\n")
    with patch('forca.open', lambda x, y: open(testfile, y)):
        palavra = palavra_secreta()
        assert palavra in ["python", "java", "ruby"]

def test_chute(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "A")
    assert chute() == "a"

def test_inicializa_letras_acertadas():
    assert inicializa_letras_acertadas("python") == ["_", "_", "_", "_", "_", "_"]

def test_adicionar_palavra(tmpdir):
    testfile = tmpdir.join("lista.txt")
    adicionar_palavra(testfile, "golang")
    with open(testfile, 'r') as f:
        assert "golang\n" in f.readlines()

def test_forca(capsys):
    forca(6)
    captured = capsys.readouterr()
    assert " ___" in captured.out
    assert "|/      |" in captured.out
    assert "|            " in captured.out

    forca(0)
    captured = capsys.readouterr()
    assert " ___" in captured.out
    assert "|/      |" in captured.out
    assert "|      (_)" in captured.out
    assert "|      /|\\" in captured.out
    assert "|      / \\" in captured.out
