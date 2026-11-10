# OpenAI directory submission

Build from the repository root with Python 3:

```sh
python scripts/package-openai-plugin.py
```

Upload `dist/musicmapp-openai-plugin.zip` to OpenAI Platform → Plugins.
The ZIP root contains `plugin.json`, `mcp.json`, and the referenced square SVG.
The full GitHub repository ZIP has a different root and is not the submission package.

## Remaining portal steps

- Sign in and select the project and verified publishing identity.
- Upload the package, connect the unauthenticated production MCP and complete domain verification using the exact token supplied by the portal.
- Resolve the current metadata/tool scan findings and provide annotation justifications.
- Run the five positive and three negative prompts in ChatGPT, record a real walkthrough, and provide its accessible URL. Direct protocol smoke tests do not replace those conversational checks.
- Confirm the privacy disclosure accurately covers MCP processing, review the policy attestations, then submit. Publish after approval.

The package deliberately contains no placeholder demo URL and does not claim approval or publication.

## Direct production checks performed

Initialization using protocol 2025-03-26, tools/list, a two-event search, public event detail, supported filters, next-cursor pagination and a nonexistent UUID were exercised successfully. All three tools advertised readOnlyHint=true and destructiveHint=false. Health, privacy and terms URLs returned HTTP 200; the legal pages returned the SPA shell, so rendered legal content still needs review.

## Demo outline

Demonstrate each positive prompt in the manifest, including following up with event details and more results. Then show the three unsupported requests (private events, ticket purchases and deletion) receiving an explanation without taking those actions.

Official requirements: https://developers.openai.com/plugins/deploy/submission
