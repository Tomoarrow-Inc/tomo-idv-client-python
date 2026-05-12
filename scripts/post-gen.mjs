/**
 * Post-generation fixup for tomo-idv-client-python.
 * Copies generated package/docs from the temporary OpenAPI output directory
 * into the manually maintained src/ layout, then removes the temporary tree.
 */
import { cpSync, existsSync, mkdirSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(__dirname, '..');
const tempRoot = join(repoRoot, '.openapi-generator-tmp');
const generatedSource = join(tempRoot, 'tomo_idv_client', 'generated');
const generatedDest = join(repoRoot, 'src', 'tomo_idv_client', 'generated');
const docsSource = join(tempRoot, 'tomo_idv_client', 'generated', 'docs');
const readmeSource = join(tempRoot, 'tomo_idv_client', 'generated_README.md');
const docsDest = join(repoRoot, 'generated-docs');

if (!existsSync(generatedSource)) {
  throw new Error(`Generated Python package not found: ${generatedSource}`);
}

mkdirSync(join(repoRoot, 'src', 'tomo_idv_client'), { recursive: true });
cpSync(generatedSource, generatedDest, { recursive: true });
rmSync(join(generatedDest, 'test'), { recursive: true, force: true });
console.log(`Copied generated package to ${generatedDest}`);

rmSync(docsDest, { recursive: true, force: true });
mkdirSync(docsDest, { recursive: true });
if (existsSync(docsSource)) {
  cpSync(docsSource, join(docsDest, 'docs'), { recursive: true });
}
if (existsSync(readmeSource)) {
  cpSync(readmeSource, join(docsDest, 'README.md'));
}
console.log(`Copied generated docs to ${docsDest}`);

rmSync(tempRoot, { recursive: true, force: true });
