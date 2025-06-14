# Solução para MCP Server no WSL

Ao tentar usar o método padrão de criação do `mcp.json` na pasta `.vscode`, encontrei o erro `Connection state: Error spawn .... ENOENT`. Após alguma pesquisa, descobri que este é um problema conhecido no VS Code, que será resolvido em uma atualização futura.

Você pode acompanhar o problema aqui: [https://github.com/microsoft/vscode/issues/251308](https://github.com/microsoft/vscode/issues/251308)

## A Solução

Como a atualização pode demorar um pouco, estou usando uma solução temporária no meu `settings.json`. Como uso o VS Code no WSL e não queria modificar o `settings.json` do Windows, estou usando a seguinte configuração:

```json
"mcp": {
    "servers": {
        "DevOpsUtilityCommands": {
            "type": "stdio",
            "command": "wsl.exe", // Invoca o subsistema WSL
            "args": [
                "/home/edipof/Documents/repo/mcp-lab/code/python-mcp/.venv/bin/python", // Comando a ser executado dentro do WSL
                "/home/edipof/Documents/repo/mcp-lab/code/python-mcp/server-mcp.py" // Caminho dentro do WSL
            ]
        }
    }
}
```

### Configuração Padrão (para quando o problema for resolvido)

Se não fosse por este problema, o `mcp.json` poderia ser criado assim:

```json
{
  "servers": {
    "DevOpsUtilityCommands": {
      "type": "stdio",
      "command": "${workspaceFolder}/code/python-mcp/.venv/bin/python",
      "args": [
        "${workspaceFolder}/code/python-mcp/server-mcp.py"
      ]
    }
  }
}
```

## Considerações Importantes

Depois de aplicar esta solução, tudo funciona como esperado. O Copilot consegue detectar o servidor MCP, e eu consigo listar contêineres Docker, executar comandos do Kubernetes e até mesmo controlar o Jenkins perfeitamente.

**Um aviso:** Estes comandos são simples e fáceis de implementar, mas devem ser usados com extremo cuidado. Neste repositório, eles são para fins de teste. Em um ambiente com acesso a sistemas críticos, a melhor abordagem é criar funções altamente restritivas.

## Planos Futuros

Este repositório é um trabalho em andamento. Adicionarei mais ferramentas ao longo do tempo, incluindo uma versão em TypeScript do servidor MCP.
