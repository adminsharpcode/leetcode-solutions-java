const { spawn } = require('child_process');
const http = require('http');

const BRAVE_EXE = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe';

console.log('[*] Spawning detached Brave process...');
const child = spawn(BRAVE_EXE, ['--remote-debugging-port=9222'], {
  detached: true,
  stdio: 'ignore'
});
child.unref();

setTimeout(() => {
  http.get('http://localhost:9222/json/version', res => {
    let body = '';
    res.on('data', c => body += c);
    res.on('end', () => {
      console.log('Status:', res.statusCode);
      console.log('Response:', body.substring(0, 150));
    });
  }).on('error', e => console.error('Error:', e.message));
}, 2500);

