<?php
/**
 * Simple router for PHP built-in server
 * Routes all requests to index.php for proper handling
 */

// Get the requested URI
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// If it's a file that exists, serve it directly
if ($uri !== '/' && file_exists(__DIR__ . $uri)) {
    return false; // Let the server handle it
}

// For root path or any other path, serve index.php
if ($uri === '/' || $uri === '') {
    require_once __DIR__ . '/index.php';
    return true;
}

// For other paths, also serve index.php (for routing)
require_once __DIR__ . '/index.php';
return true;
