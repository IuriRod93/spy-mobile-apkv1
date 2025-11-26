# TODO - Configuração do GitHub Actions para Build APK

## Tarefas Concluídas
- [x] Criar diretório .github/workflows
- [x] Criar workflow build-apk.yml para GitHub Actions
- [x] Configurar workflow com:
  - Configuração do Python 3.9
  - Instalação de dependências do sistema para Android
  - Instalação do buildozer e cython
  - Instalação de dependências Python do projeto
  - Configuração do Android SDK
  - Comando de build do APK
  - Upload do artefato APK

## Próximos Passos
- [ ] Testar o workflow fazendo push para o repositório
- [ ] Verificar se o APK é gerado corretamente
- [ ] Ajustar configurações se necessário (versão do Android, dependências, etc.)
- [ ] Documentar o processo de uso do GitHub Actions

## Notas
- O workflow está configurado para rodar em push e pull requests nas branches main/master
- Usa Ubuntu latest como runner
- Instala Android SDK automaticamente
- Faz upload do APK como artefato após o build
