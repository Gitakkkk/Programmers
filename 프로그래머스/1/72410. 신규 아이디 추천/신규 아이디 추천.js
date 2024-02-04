function solution(new_id) {
    let result = new_id
    .toLowerCase()
    .replace(/[^a-z0-9-_.]/g, '')
    .replace(/\.{2,}/g, '.')
    .replace(/^\.|\.$/, '')
    .replace(/^$/g, 'a')
    .slice(0,15)
    .replace(/\.$/, '')
    return result.padEnd(3, result[result.length-1])
}