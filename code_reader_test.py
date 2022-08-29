from App.AppFrames.Controllers.CodeReaders.CodeReaders import get_code_readers

players = get_code_readers()
print(players)
reader = players["Magellan"]["import"]({"NombrePuerto":"USB"})