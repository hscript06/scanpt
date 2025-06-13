echo "🔧 Instalando scanpt..."
if [ "$EUID" -ne 0 ]; then
    echo "❌ Por favor, ejecuta este script como root (usa sudo)"
    exit 1
fi
SOURCE="./scanpt"
DEST="/usr/local/bin/scanpt"
cp "$SOURCE" "$DEST"
chmod +x "$DEST"

echo "✅ Instalación completada. Ya puedes usar el comando: scanpt"
