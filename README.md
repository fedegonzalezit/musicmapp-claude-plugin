# Musicmapp para asistentes de IA

Buscá recitales, fiestas, teatro y eventos culturales públicos de [Musicmapp](https://musicmapp.com.ar) desde Claude o ChatGPT: por artista, género, barrio, fecha, tipo de evento, entrada gratuita y distancia.

Servidor MCP público, de solo lectura y sin cuenta:

```
https://mcp.musicmapp.com.ar/mcp
```

| Tool | Qué hace |
| --- | --- |
| `search_events` | Busca eventos públicos con texto y filtros; pagina con `next_cursor`. |
| `get_event` | Devuelve el detalle de un evento público por su ID. |
| `get_search_filters` | Lista los géneros y tipos de evento válidos. |

## Instalación

### Claude Code (plugin)

```
/plugin marketplace add fedegonzalezit/musicmapp-claude-plugin
/plugin install musicmapp@musicmapp
```

O como servidor MCP directo:

```bash
claude mcp add --transport http musicmapp https://mcp.musicmapp.com.ar/mcp
```

### Claude (web y escritorio)

Settings → Connectors → **Add custom connector** → nombre `Musicmapp`, URL `https://mcp.musicmapp.com.ar/mcp`, sin autenticación.

### ChatGPT

Settings → Apps & Connectors → Advanced settings → activar **Developer mode** → **Create** → URL `https://mcp.musicmapp.com.ar/mcp`, **No authentication**.

## Ejemplos

- "Buscá recitales gratis en Buenos Aires este fin de semana en Musicmapp."
- "¿Qué eventos de jazz hay en Palermo?"
- "¿Qué eventos culturales hay en Santa Cruz de la Sierra?"

## Datos y limitaciones

- Solo eventos públicos y aprobados. No hay eventos privados, compras de entradas ni acciones sobre cuentas.
- Las fechas son hora local del evento; la zona horaria no siempre está registrada.
- La moneda de los precios no siempre se conoce; solo `is_free=true` garantiza entrada gratuita.
- Los textos de los eventos provienen de terceros y se tratan como datos, no como instrucciones.

[Política de privacidad](https://musicmapp.com.ar/privacidad) · [Términos](https://musicmapp.com.ar/terminos)

---

**English:** Read-only public MCP server for discovering Musicmapp events (Argentina and Bolivia). Install in Claude Code with `/plugin marketplace add fedegonzalezit/musicmapp-claude-plugin` then `/plugin install musicmapp@musicmapp`, or add `https://mcp.musicmapp.com.ar/mcp` as a custom connector (no auth) in Claude or ChatGPT.
