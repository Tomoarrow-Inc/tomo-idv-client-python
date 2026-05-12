/**
 * Pre-generation cleanup for tomo-idv-client-python.
 * Removes generated code and the temporary OpenAPI output directory.
 */
import { rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(__dirname, '..');

const dirsToClean = [
  join(repoRoot, '.openapi-generator-tmp'),
  join(repoRoot, 'generated-docs'),
  join(repoRoot, 'src', 'tomo_idv_client', 'generated'),
];

for (const dir of dirsToClean) {
  rmSync(dir, { recursive: true, force: true });
  console.log(`Cleaned ${dir}`);
}
