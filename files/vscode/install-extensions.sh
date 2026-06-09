EXTENSIONS_PATH=~/.dotfiles/files/vscode/code-extensions

echo "Installing code extensions..."
cat $EXTENSIONS_PATH | while read line
do
	code --install-extension "$line"
done
